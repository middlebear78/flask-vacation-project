import DestinationSection from '../components/home/DestinationSection'

const services = [
  { icon: 'fa-globe', title: 'WorldWide Tours', desc: 'Discover amazing destinations with our expertly crafted tours, ensuring unforgettable experiences and exciting adventures.' },
  { icon: 'fa-hotel', title: 'Hotel Reservation', desc: 'Find and book top accommodations effortlessly, with our curated selection ensuring comfort, convenience, and exceptional stays.' },
  { icon: 'fa-user', title: 'Travel Guides', desc: 'Explore detailed guides with insider tips and local recommendations, helping you navigate and enjoy every destination.' },
  { icon: 'fa-cog', title: 'Event Management', desc: 'Organize and execute memorable events with our expert planning, ensuring seamless coordination and exceptional experiences for all.' },
  { icon: 'fa-globe', title: 'Recreational events for kids', desc: 'Enjoy a variety of fun and engaging events designed to entertain and delight children of all ages.' },
  { icon: 'fa-hotel', title: 'Fun and sporty activity', desc: 'Engage in exciting and energetic activities designed for fun, fitness, and adventure during your stay.' },
  { icon: 'fa-user', title: 'Special tours', desc: 'Embark on unique and exclusive tours tailored to offer extraordinary experiences and unforgettable moments.' },
  { icon: 'fa-cog', title: "Resort's restaurants", desc: "Savor exceptional dining experiences at our resort's restaurants, offering a diverse menu with gourmet dishes and local flavors." },
]

export default function HomePage() {
  return (
    <>
      {/* Service Start */}
      <div className="container-xxl py-5">
        <div className="container">
          <div className="text-center" data-aos="fade-up">
            <h6 className="section-title bg-white text-center text-primary px-3">Services</h6>
            <h1 className="mb-5">Our Services</h1>
          </div>
          <div className="row g-4">
            {services.map((s, i) => (
              <div key={i} className="col-lg-3 col-sm-6" data-aos="fade-up" data-aos-delay={((i % 4) * 200 + 100)}>
                <div className="service-item rounded pt-3">
                  <div className="p-4">
                    <i className={`fa fa-3x ${s.icon} text-primary mb-4`}></i>
                    <h5>{s.title}</h5>
                    <p>{s.desc}</p>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
      {/* Service End */}

      <DestinationSection />
    </>
  )
}
