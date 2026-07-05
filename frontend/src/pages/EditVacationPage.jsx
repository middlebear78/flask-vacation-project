import { useState, useEffect } from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import * as api from '../api/client'
import { useFlash } from '../context/FlashContext'

export default function EditVacationPage() {
  const { id } = useParams()
  const navigate = useNavigate()
  const { showFlash } = useFlash()
  const [countries, setCountries] = useState([])
  const [form, setForm] = useState({
    vacation_name: '', price: '', start_date: '', end_date: '',
    country: '', vacation_description: '',
  })
  const [currentImg, setCurrentImg] = useState(null)
  const [imageFile, setImageFile] = useState(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    Promise.all([api.getVacation(id), api.getCountries()])
      .then(([vacation, countries]) => {
        setForm({
          vacation_name: vacation.vacation_name,
          price: vacation.price,
          start_date: vacation.start_date,
          end_date: vacation.end_date,
          country: vacation.country_name,
          vacation_description: vacation.vacation_description || '',
        })
        setCurrentImg(vacation.vacation_img)
        setCountries(countries)
      })
      .catch(err => showFlash(err.message, 'error'))
      .finally(() => setLoading(false))
  }, [id])

  function handleChange(e) {
    setForm({ ...form, [e.target.name]: e.target.value })
  }

  function handleImageChange(e) {
    const file = e.target.files[0]
    setImageFile(file)
    if (file) {
      const reader = new FileReader()
      reader.onload = ev => {
        const img = document.getElementById('current_image')
        if (img) img.src = ev.target.result
      }
      reader.readAsDataURL(file)
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
      await api.updateVacation(id, fd)
      showFlash('Vacation updated successfully!', 'success')
      navigate('/vacations')
    } catch (err) {
      showFlash(err.message, 'error')
    }
  }

  if (loading) return null

  return (
    <div className="container-xxl py-5" data-aos="fade-up" id="edit-section">
      <div className="container">
        <div className="booking p-5">
          <div className="row g-5 align-items-center">
            <div className="col-md-6">
              <h1 className="text-white mb-4">Edit Vacation - {id}</h1>
              <form onSubmit={handleSubmit}>
                <div className="row g-3">
                  <div className="col-md-6">
                    <div className="form-floating">
                      <input type="text" className="form-control bg-transparent" name="vacation_name"
                        placeholder="Vacation Name" value={form.vacation_name} onChange={handleChange}
                        minLength="2" maxLength="100" required />
                      <label>Vacation Name</label>
                    </div>
                  </div>
                  <div className="col-md-6">
                    <div className="form-floating">
                      <input type="number" className="form-control bg-transparent" name="price"
                        placeholder="Price" value={form.price} onChange={handleChange}
                        step="0.01" min="0" max="10000" required />
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
                        placeholder="End Date" value={form.end_date} onChange={handleChange} required />
                      <label>End Date</label>
                    </div>
                  </div>
                  <div className="col-md-6">
                    <div className="form-floating">
                      <select className="form-select bg-transparent" name="country"
                        value={form.country} onChange={handleChange} required>
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
                    <button className="btn btn-outline-light w-100 py-3" type="submit">Update Vacation</button>
                  </div>
                </div>
              </form>
            </div>
            <div className="col-md-6 text-center">
              <div className="form-group">
                <label className="text-white"><i className="fas fa-image"></i> Current Image:</label>
                <div>
                  <img id="current_image" src={api.vacationImageUrl(currentImg)} alt="Current Vacation Image" className="img-fluid" />
                </div>
              </div>
              <div className="form-group mt-3">
                <label htmlFor="preview_image" className="text-white"><i className="fas fa-image"></i> New Image:</label>
                <input type="file" className="form-control bg-transparent" accept="image/*"
                  id="preview_image" onChange={handleImageChange} />
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}
