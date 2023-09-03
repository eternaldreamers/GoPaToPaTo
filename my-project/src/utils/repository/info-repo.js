import { db } from "@/utils/mongodb";

const Info = db.Info;

export const infoRepo = {
  create: async (params) => {
    if (await Info.findOne({ email: params.email })) {
      throw 'Email "' + params.email + '" is already taken';
    }

    const info = new Info(params);

    await info.save();
  },
  getOne: async (email) => {
    const record = Info.findOne({ email })
    return record;
  },
};
