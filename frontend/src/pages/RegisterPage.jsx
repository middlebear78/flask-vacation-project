import { useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { useAuth } from '../context/AuthContext'
import { useFlash } from '../context/FlashContext'

export default function RegisterPage() {
  const [firstName, setFirstName] = useState('')
  const [lastName, setLastName] = useState('')
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const { register } = useAuth()
  const { showFlash } = useFlash()
  const navigate = useNavigate()

  async function handleSubmit(e) {
    e.preventDefault()
    try {
      await register(firstName, lastName, email, password)
      showFlash('Registration successful!', 'success')
      navigate('/vacations')
    } catch (err) {
      showFlash(err.message, 'error')
    }
  }

  return (
    <div className="container-xxl py-5" data-aos="fade-up" id="register-section">
      <div className="container">
        <div className="booking p-5">
          <div className="row g-5 align-items-center">
            <div className="col-md-6 text-white">
              <h6 className="text-white text-uppercase">PassPort The World</h6>
              <h1 className="text-white mb-4">Welcome</h1>
              <p className="mb-4"></p>
              <p className="mb-4">Already have an account?</p>
              <Link className="btn btn-outline-light py-3 px-5 mt-2" to="/login">Sign In</Link>
            </div>
            <div className="col-md-6">
              <h1 className="text-white mb-4">Register For An Account</h1>
              <form onSubmit={handleSubmit}>
                <div className="row g-3">
                  <div className="col-md-6">
                    <div className="form-floating">
                      <input type="text" className="form-control bg-transparent" id="first_name"
                        placeholder="Your first Name" value={firstName}
                        onChange={e => setFirstName(e.target.value)} required />
                      <label htmlFor="first_name">First Name</label>
                    </div>
                  </div>
                  <div className="col-md-6">
                    <div className="form-floating">
                      <input type="text" className="form-control bg-transparent" id="last_name"
                        placeholder="Your last Name" value={lastName}
                        onChange={e => setLastName(e.target.value)} required />
                      <label htmlFor="last_name">Last Name</label>
                    </div>
                  </div>
                  <div className="col-md-6">
                    <div className="form-floating">
                      <input type="email" className="form-control bg-transparent" id="email"
                        placeholder="Your Email" value={email}
                        onChange={e => setEmail(e.target.value)} required />
                      <label htmlFor="email">Your Email</label>
                    </div>
                  </div>
                  <div className="col-md-6">
                    <div className="form-floating">
                      <input type="password" className="form-control bg-transparent" id="password"
                        placeholder="Your Password" value={password}
                        onChange={e => setPassword(e.target.value)}
                        minLength="4" required />
                      <label htmlFor="password">Password</label>
                    </div>
                  </div>
                  <div className="col-12">
                    <button className="btn btn-outline-light w-100 py-3" type="submit">Sign up</button>
                  </div>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}
