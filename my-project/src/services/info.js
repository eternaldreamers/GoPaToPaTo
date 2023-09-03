import { fetchWrapper } from "@/utils";

async function create(args) {
  await fetchWrapper.post("/api/info", args);
}

export const infoService = {
  create,
};
