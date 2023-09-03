import { useForm } from "react-hook-form";
import { yupResolver } from "@hookform/resolvers/yup";
import * as Yup from "yup";
import Router from "next/router";

export default function Home() {
  const validationSchema = Yup.object().shape({
    email: Yup.string().email().required("Email is required"),
    firstName: Yup.string().required("First Name is required"),
    lastName: Yup.string().required("Last Name is required"),
  });

  const formOptions = { resolver: yupResolver(validationSchema) };

  const { register, handleSubmit } = useForm(formOptions);

  async function onSubmit(data) {
    fetch("/api/info", {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    }).then(() => Router.push(`/info/${data.email}`));
  }

  return (
    <div className="vh-100 d-flex justify-content-center align-items-center">
      <div className="container">
        <div className="row d-flex justify-content-center">
          <div className="col-12 col-md-8 col-lg-6">
            <div className="card bg-white">
              <div className="card-body p-5">
                <form
                  className="mb-3 mt-md-4"
                  onSubmit={handleSubmit(onSubmit)}
                >
                  <h2 className="fw-bold mb-2 text-uppercase text-center">
                    Project
                  </h2>
                  <p className="mb-5 text-center">
                    Please enter your information!
                  </p>
                  <div className="mb-3">
                    <label htmlFor="email" className="form-label ">
                      Email address
                    </label>
                    <input
                      type="email"
                      {...register("email")}
                      className="form-control"
                      id="email"
                    />
                  </div>
                  <div className="mb-3">
                    <label htmlFor="firstName" className="form-label ">
                      firstName
                    </label>
                    <input
                      type="text"
                      className="form-control"
                      {...register("firstName")}
                      id="firstName"
                    />
                  </div>
                  <div className="mb-3">
                    <label htmlFor="lastName" className="form-label ">
                      lastName
                    </label>
                    <input
                      type="text"
                      className="form-control"
                      {...register("lastName")}
                      id="lastName"
                    />
                  </div>
                  <div className="d-grid">
                    <button className="btn btn-outline-dark" type="submit">
                      Submit
                    </button>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
