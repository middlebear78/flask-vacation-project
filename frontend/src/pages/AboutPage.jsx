const teamMembers = [
  { name: 'Uri and Shani shnetzer', role: 'C.E.O', img: '/images/uri-and-shani.jpg', alt: 'uri and shani' },
  { name: 'Almog Moskovitch', role: 'Lead Guide', img: '/images/almog.jpg', alt: 'almog' },
  { name: 'Hernan Kadzor', role: 'Lead guide and Meat chef', img: '/images/hernan.jpg', alt: 'hernan' },
  { name: 'Elisha Soloway', role: 'Lead Host', img: '/images/elisha.jpg', alt: 'elisha' },
]

export default function AboutPage() {
  return (
    <>
      {/* About Start */}
      <div className="container-xxl py-5" id="about-section">
        <div className="container">
          <div className="row g-5">
            <div className="col-lg-6" data-aos="fade-up" style={{ minHeight: '400px' }}>
              <div className="position-relative h-100">
                <img className="img-fluid position-absolute w-100 h-100" src="/images/about.jpg" alt="" style={{ objectFit: 'cover' }} />
              </div>
            </div>
            <div className="col-lg-6" data-aos="fade-up" data-aos-delay="200">
              <h6 className="section-title bg-white text-start text-primary pe-3">About Us</h6>
              <h1 className="mb-4">Welcome to <span className="text-primary">PassPort the World</span></h1>
              <p className="mb-4">your ultimate destination for unforgettable travel experiences. We specialize in creating tailor-made journeys that allow you to explore the world's most beautiful and fascinating destinations..</p>
              <p className="mb-4">At Passport the World, we believe that travel should be seamless and enriching. Our team of experienced travel experts is dedicated to curating the perfect trip for you, whether it's a romantic getaway, a family vacation, or an adventure of a lifetime.</p>
              <div className="row gy-2 gx-4 mb-4">
                {['First Class Flights', 'Handpicked Hotels', '5 Star Accommodations', 'Latest Model Vehicles', '150 Premium City Tours', '24/7 Service'].map((item, i) => (
                  <div key={i} className="col-sm-6">
                    <p className="mb-0"><i className="fa fa-arrow-right text-primary me-2"></i>{item}</p>
                  </div>
                ))}
              </div>
              <a className="btn btn-primary py-3 px-5 mt-2" href="">Read More</a>
            </div>
          </div>
        </div>
      </div>
      {/* About End */}

      {/* Team Start */}
      <div className="container-xxl py-5">
        <div className="container">
          <div className="text-center" data-aos="fade-up">
            <h6 className="section-title bg-white text-center text-primary px-3">Travel Guides</h6>
            <h1 className="mb-5">Meet Our Guides</h1>
          </div>
          <div className="row g-4">
            {teamMembers.map((m, i) => (
              <div key={i} className="col-lg-3 col-md-6" data-aos="fade-up" data-aos-delay={i * 200 + 100}>
                <div className="team-item">
                  <div className="overflow-hidden team-image-wrapper">
                    <img className="img-fluid team-image" src={m.img} alt={m.alt} />
                  </div>
                  <div className="position-relative d-flex justify-content-center" style={{ marginTop: '-19px' }}>
                    <a className="btn btn-square mx-1" href=""><i className="fab fa-facebook-f"></i></a>
                    <a className="btn btn-square mx-1" href=""><i className="fab fa-twitter"></i></a>
                    <a className="btn btn-square mx-1" href=""><i className="fab fa-instagram"></i></a>
                  </div>
                  <div className="text-center p-4">
                    <h5 className="mb-0">{m.name}</h5>
                    <small>{m.role}</small>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
      {/* Team End */}
    </>
  )
}
