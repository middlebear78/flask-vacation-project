import { useEffect, useRef } from 'react'
import { NavLink, Link, useNavigate } from 'react-router-dom'
import { useAuth } from '../../context/AuthContext'

export default function Navbar() {
  const { user, logout } = useAuth()
  const navigate = useNavigate()
  const navRef = useRef(null)

  useEffect(() => {
    function onScroll() {
      const nav = navRef.current
      if (!nav) return
      if (window.scrollY > 45) {
        nav.classList.add('sticky-top', 'shadow-sm')
      } else {
        nav.classList.remove('sticky-top', 'shadow-sm')
      }
    }
    window.addEventListener('scroll', onScroll)
    return () => window.removeEventListener('scroll', onScroll)
  }, [])

  // Dropdown hover for desktop
  useEffect(() => {
    function setupHover() {
      const dropdowns = document.querySelectorAll('.dropdown')
      dropdowns.forEach(dd => {
        if (window.matchMedia('(min-width: 992px)').matches) {
          dd.addEventListener('mouseenter', handleEnter)
          dd.addEventListener('mouseleave', handleLeave)
        } else {
          dd.removeEventListener('mouseenter', handleEnter)
          dd.removeEventListener('mouseleave', handleLeave)
        }
      })
    }
    function handleEnter() {
      this.classList.add('show')
      const toggle = this.querySelector('.dropdown-toggle')
      const menu = this.querySelector('.dropdown-menu')
      if (toggle) toggle.setAttribute('aria-expanded', 'true')
      if (menu) menu.classList.add('show')
    }
    function handleLeave() {
      this.classList.remove('show')
      const toggle = this.querySelector('.dropdown-toggle')
      const menu = this.querySelector('.dropdown-menu')
      if (toggle) toggle.setAttribute('aria-expanded', 'false')
      if (menu) menu.classList.remove('show')
    }
    setupHover()
    window.addEventListener('resize', setupHover)
    return () => window.removeEventListener('resize', setupHover)
  }, [user])

  async function handleLogout(e) {
    e.preventDefault()
    await logout()
    navigate('/login')
  }

  return (
    <div className="container-fluid position-relative p-0">
      <nav ref={navRef} className="navbar navbar-expand-lg navbar-light px-4 px-lg-5 py-3 py-lg-0">
        <Link to="/" className="navbar-brand p-0">
          <h1 className="text-primary m-0 text-blue">
            <i className="fa fa-map-marker-alt me-3"></i>Passport The World
          </h1>
        </Link>
        <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarCollapse">
          <span className="fa fa-bars"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarCollapse">
          <div className="navbar-nav ms-auto py-0">
            <NavLink to="/" className="nav-item nav-link" end>Home</NavLink>
            <NavLink to="/about" className="nav-item nav-link">About</NavLink>
            {user && user.is_admin && (
              <>
                <NavLink to="/vacations" className="nav-item nav-link">Vacations</NavLink>
                <div className="nav-item dropdown">
                  <a href="#" className="nav-link dropdown-toggle" data-bs-toggle="dropdown">ADMIN</a>
                  <div className="dropdown-menu m-0">
                    <Link to="/vacations" className="dropdown-item">Manage Vacations</Link>
                    <Link to="/vacations/new" className="dropdown-item">Add a Vacation</Link>
                  </div>
                </div>
              </>
            )}
            {user && !user.is_admin && (
              <NavLink to="/vacations" className="nav-item nav-link">Vacations</NavLink>
            )}
          </div>
          {user ? (
            <>
              <span className="nav-link disabled-link current-user">
                Hello {user.first_name} {user.last_name}
              </span>
              <a href="#" onClick={handleLogout} className="btn btn-primary rounded-pill py-2 px-4">Logout</a>
            </>
          ) : (
            <>
              <Link to="/login" className="btn btn-primary rounded-pill py-2 px-4">Login</Link>
              <span className="nav-item nav-link"> | </span>
              <Link to="/register" className="btn btn-primary rounded-pill py-2 px-4">Register</Link>
            </>
          )}
        </div>
      </nav>

      <div className="container-fluid bg-primary py-5 mb-5 hero-header">
        <div className="container py-5">
          <div className="row justify-content-center py-5">
            <div className="col-lg-10 pt-lg-5 mt-lg-5 text-center">
              <h1 className="display-3 text-white mb-3 animated slideInDown">Enjoy Your Vacation With Us</h1>
              <p className="fs-4 text-white mb-4 animated slideInDown">
                Your Gateway to Unforgettable Journeys and Endless Adventures. Explore, Dream, Discover.
              </p>
              <div className="position-relative w-75 mx-auto animated slideInDown">
                <input className="form-control border-0 rounded-pill w-100 py-3 ps-4 pe-5" type="text" placeholder="Eg: Thailand" />
                <button type="button" className="btn btn-primary rounded-pill py-2 px-4 position-absolute top-0 end-0 me-2" style={{ marginTop: '7px' }}>
                  Search
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}
