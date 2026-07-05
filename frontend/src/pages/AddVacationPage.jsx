import { useState, useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import * as api from '../api/client'
import { useFlash } from '../context/FlashContext'

export default function AddVacationPage() {
  const [countries, setCountries] = useState([])
  const [form, setForm] = useState({
    vacation_name: '', price: '', start_date: '', end_date: '',
    country: '', vacation_description: '',
  })
  const [imageFile, setImageFile] = useState(null)
  const [preview, setPreview] = useState(null)
  const { showFlash } = useFlash()
  const navigate = useNavigate()

  useEffect(() => {
    api.getCountries().then(setCountries).catch(() => {})
  }, [])

  function handleChange(e) {
    setForm({ ...form, [e.target.name]: e.target.value })
  }

  function handleImageChange(e) {
    const file = e.target.files[0]
    setImageFile(file)
    if (file) {
      const reader = new FileReader()
      reader.onload = ev => setPreview(ev.target.result)
      reader.readAsDataURL(file)
    } else {
      setPreview(null)
    }
  }

  async function handleSubmit(e) {
    e.preventDefault()
    const fd = new FormData()
    fd.append('vacation_name', form.vacation_name)
    fd.append('vacation_description', form.vacation_description)
    fd.append('start_date', form.start_date)
    fd.append('end_date', form.end_date)
    fd.append('price', form.price)
    fd.append('country', form.country)
    if (imageFile) fd.append('vacation_image', imageFile)

    try {
      await api.createVacation(fd)
      showFlash('Vacation added successfully!', 'success')
      navigate('/vacations')
    } catch (err) {
      showFlash(err.message, 'error')
    }
  }

  return (
    <div className="container-xxl py-5" data-aos="fade-up" id="add-section">
      <div className="container">
        <div className="booking p-5">
          <div className="row g-5 align-items-center">
            <div className="col-md-6">
              <h1 className="text-white mb-4">Add a Vacation</h1>
              <form onSubmit={handleSubmit}>
                <div className="row g-3">
                  <div className="col-md-6">
                    <div className="form-floating">
                      <input type="text" className="form-control bg-transparent" name="vacation_name"
                        placeholder="Vacation Name" value={form.vacation_name} onChange={handleChange} required />
                      <label>Vacation Name</label>
                    </div>
                  </div>
                  <div className="col-md-6">
                    <div className="form-floating">
                      <input type="number" className="form-control bg-transparent" name="price"
                        placeholder="Price" value={form.price} onChange={handleChange}
                        min="0" max="10000" required />
                      <label>Price</label>
                    </div>
                  </div>
                  <div className="col-md-6">
                    <div className="form-floating">
                      <input type="date" className="form-control bg-transparent" name="start_date"
                        placeholder="Start Date" value={form.start_date} onChange={handleChange} required />
                      <label>Start Date</label>
                    </div>
                  </div>
                  <div className="col-md-6">
                    <div className="form-floating">
                      <input type="date" className="form-control bg-transparent" name="end_date"
                        placeholder="End Date" value={form.end_date} onChange={handleChange} />
                      <label>End Date</label>
                    </div>
                  </div>
                  <div className="col-md-6">
                    <div className="form-floating">
                      <select className="form-select bg-transparent" name="country"
                        value={form.country} onChange={handleChange} required>
                        <option value="">Select country</option>
                        {countries.map(c => (
                          <option key={c.country_id} value={c.country_name}>{c.country_name}</option>
                        ))}
                      </select>
                      <label>Country</label>
                    </div>
                  </div>
                  <div className="col-12">
                    <div className="form-floating">
                      <textarea className="form-control bg-transparent" name="vacation_description"
                        placeholder="Vacation Description" style={{ height: '100px' }}
                        value={form.vacation_description} onChange={handleChange} required></textarea>
                      <label>Vacation Description</label>
                    </div>
                  </div>
                  <div className="col-12">
                    <button className="btn btn-outline-light w-100 py-3" type="submit">Add Vacation</button>
                  </div>
                </div>
              </form>
            </div>
            <div className="col-md-6 text-center">
              <div className="form-group">
                <label htmlFor="preview_image" className="text-white">
                  <i className="fas fa-image"></i> Preview Image:
                </label>
                <input type="file" className="form-control bg-transparent" accept="image/*"
                  id="preview_image" onChange={handleImageChange} required />
              </div>
              <div className="image-preview">
                {preview && <img src={preview} alt="Preview" style={{ maxWidth: '100%', maxHeight: '400px' }} />}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}
