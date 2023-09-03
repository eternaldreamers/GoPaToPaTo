import getConfig from "next/config";
import mongoose from "mongoose";

const { serverRuntimeConfig } = getConfig();
const Schema = mongoose.Schema;

mongoose.connect(serverRuntimeConfig.connectionString);
mongoose.Promise = global.Promise;

function infoModel() {
  const schema = new Schema(
    {
      email: { type: String, required: true },
      firstName: { type: String, required: true },
      lastName: { type: String, required: true },
    },
    {
      timestamps: true,
    }
  );

  return mongoose.models.Info || mongoose.model("Info", schema);
}

export const db = {
  Info: infoModel(),
};
