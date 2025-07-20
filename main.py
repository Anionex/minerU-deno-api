import { serve } from "https://deno.land/std@0.204.0/http/server.ts";

serve(async (req: Request) => {
  const url = new URL(req.url);
  const pathname = url.pathname;

  if (req.method === "POST" && pathname === "/parse-and-return") {
    const clientHeaders = req.headers;
    const body = await req.text(); // 保留原始体
    const headers = new Headers({
      "Content-Type": "application/json",
      "Authorization": clientHeaders.get("Authorization") || "",
    });

    // Step 1: 请求创建任务
    const mineruResp = await fetch("https://mineru.net/api/v4/extract/task", {
      method: "POST",
      headers,
      body,
    });

    const mineruJson = await mineruResp.json();
    const task_id = mineruJson?.data?.task_id;

    if (!task_id) {
      return new Response(JSON.stringify(mineruJson), {
        status: 500,
        headers: { "Content-Type": "application/json" },
      });
    }

    // Step 2: 轮询任务状态
    for (let i = 0; i < 20; i++) {
      await new Promise((res) => setTimeout(res, 2000)); // 等待 2 秒

      const statusResp = await fetch(`https://mineru.net/api/v4/extract/task/${task_id}`, {
        method: "GET",
        headers,
      });

      const statusJson = await statusResp.json();
      const state = statusJson?.data?.state;

      if (state === "done" || state === "failed") {
        return new Response(JSON.stringify(statusJson), {
          status: 200,
          headers: { "Content-Type": "application/json" },
        });
      }
    }

    return new Response(JSON.stringify({ error: "任务超时未完成" }), {
      status: 504,
      headers: { "Content-Type": "application/json" },
    });
  }

  return new Response("Not Found", { status: 404 });
});
