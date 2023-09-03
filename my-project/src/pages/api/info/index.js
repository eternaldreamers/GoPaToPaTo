import { apiHandler, infoRepo } from "@/utils";

async function create(req, res) {
  await infoRepo.create(req.body);
  return res.status(200).json({});
}

export default apiHandler({
  post: create,
});
