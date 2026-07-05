export default function DestinationSection() {
  return (
    <div className="container-xxl py-5 destination">
      <div className="container">
        <div className="text-center" data-aos="fade-up">
          <h6 className="section-title bg-white text-center text-primary px-3">Destination</h6>
          <h1 className="mb-5">Popular Destination</h1>
        </div>
        <div className="row g-3">
          <div className="col-lg-7 col-md-6">
            <div className="row g-3">
              <div className="col-lg-12 col-md-12" data-aos="zoom-in">
                <a className="position-relative d-block overflow-hidden" href="">
                  <img className="img-fluid" src="/images/destination-1.jpg" alt="" />
                  <div className="bg-white text-danger fw-bold position-absolute top-0 start-0 m-3 py-1 px-2">30% OFF</div>
                  <div className="bg-white text-primary fw-bold position-absolute bottom-0 end-0 m-3 py-1 px-2">Thailand</div>
                </a>
              </div>
              <div className="col-lg-6 col-md-12" data-aos="zoom-in" data-aos-delay="200">
                <a className="position-relative d-block overflow-hidden" href="">
                  <img className="img-fluid" src="/images/destination-2.jpg" alt="" />
                  <div className="bg-white text-danger fw-bold position-absolute top-0 start-0 m-3 py-1 px-2">25% OFF</div>
                  <div className="bg-white text-primary fw-bold position-absolute bottom-0 end-0 m-3 py-1 px-2">Malaysia</div>
                </a>
              </div>
              <div className="col-lg-6 col-md-12" data-aos="zoom-in" data-aos-delay="400">
                <a className="position-relative d-block overflow-hidden" href="">
                  <img className="img-fluid" src="/images/destination-3.jpg" alt="" />
                  <div className="bg-white text-danger fw-bold position-absolute top-0 start-0 m-3 py-1 px-2">35% OFF</div>
                  <div className="bg-white text-primary fw-bold position-absolute bottom-0 end-0 m-3 py-1 px-2">Australia</div>
                </a>
              </div>
            </div>
          </div>
          <div className="col-lg-5 col-md-6" data-aos="zoom-in" data-aos-delay="600" style={{ minHeight: '350px' }}>
            <a className="position-relative d-block h-100 overflow-hidden" href="">
              <img className="img-fluid position-absolute w-100 h-100" src="/images/destination-4.jpg" alt="" style={{ objectFit: 'cover' }} />
              <div className="bg-white text-danger fw-bold position-absolute top-0 start-0 m-3 py-1 px-2">20% OFF</div>
              <div className="bg-white text-primary fw-bold position-absolute bottom-0 end-0 m-3 py-1 px-2">Indonesia</div>
            </a>
          </div>
        </div>
      </div>
    </div>
  )
}
