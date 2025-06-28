import { vitePlugin as remix } from "@remix-run/dev";
import { defineConfig } from "vite";




declare module "@remix-run/node" {
  interface Future {
    v3_singleFetch: true;
  }
}

export default defineConfig({
  plugins: [remix()],
});
