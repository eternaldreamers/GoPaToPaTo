import { apiHandler, infoRepo } from "@/utils";

async function getOne(req, res) {
  const info = await infoRepo.getOne(req.query.email);

  if (!info) throw "Info not found";

  return res.status(200).json(info);
}

export default apiHandler({
  get: getOne,
});
