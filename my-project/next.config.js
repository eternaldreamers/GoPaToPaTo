/** @type {import('next').NextConfig} */
const nextConfig = {
  serverRuntimeConfig: {
    connectionString: "mongodb://localhost/project",
  },
};

module.exports = nextConfig;
