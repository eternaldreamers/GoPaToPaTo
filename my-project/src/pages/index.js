import Router from "next/router";

export default function Index() {
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
                    Please enter your login and password!
                  </p>
                  <div className="mb-3">
                    <label htmlFor="email" className="form-label ">
                      Email address
                    </label>
                    <input
                      type="email"
                      className="form-control"
                      id="email"
                      placeholder="name@example.com"
                    />
                  </div>
                  <div className="mb-3">
                    <label htmlFor="password" className="form-label ">
                      Password
                    </label>
                    <input
                      type="password"
                      className="form-control"
                      id="password"
                      placeholder="*******"
                    />
                  </div>
                  <div className="d-grid">
                    <button className="btn btn-outline-dark" type="submit">
                      Login
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
