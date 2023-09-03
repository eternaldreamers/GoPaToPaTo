import Router from "next/router";
import { useState, useEffect } from "react";
import { useRouter } from "next/router";

export default function Home() {
  const router = useRouter();
  const [data, setData] = useState(null);
  const [isLoading, setLoading] = useState(true);

  useEffect(() => {
    const { email } = router.query;

    fetch(`/api/info/${email}`)
      .then((res) => res.json())
      .then((data) => {
        setData(data);
        setLoading(false);
      });
  }, [router]);

  if (!data) {
    return <div>Could not load data correctly.</div>;
  }

  if (isLoading) {
    return <div>Loading...</div>;
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
                  onSubmit={(e) => {
                    e.preventDefault();
                    e.stopPropagation();
                    Router.push("/home");
                  }}
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
                    <label className="form-control">{router.query.email}</label>
                  </div>
                  <div className="mb-3">
                    <label htmlFor="firtName" className="form-label ">
                      firstName
                    </label>
                    <label className="form-control">{data.firstName}</label>
                  </div>
                  <div className="mb-3">
                    <label htmlFor="lastName" className="form-label ">
                      lastName
                    </label>
                    <label className="form-control">{data.lastName}</label>
                  </div>
                  <div className="d-grid">
                    <button className="btn btn-outline-dark" type="submit">
                      Back
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
