import { useState, useEffect } from 'react'
import * as api from '../api/client'
import VacationCard from '../components/vacations/VacationCard'

export default function VacationsPage() {
  const [vacations, setVacations] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    api.getVacations()
      .then(setVacations)
      .catch(() => {})
      .finally(() => setLoading(false))
  }, [])

  function handleDelete(id) {
    setVacations(prev => prev.filter(v => v.vacation_id !== id))
  }

  if (loading) return null

  return (
    <div className="container-xxl py-5" id="vacations-section">
      <div className="container">
        <div className="text-center" data-aos="fade-up">
          <h6 className="section-title bg-white text-center text-primary px-3">Vacations</h6>
          <h1 className="mb-5">Our Awesome Vacations</h1>
        </div>
        <div className="row g-4 justify-content-center">
          {vacations.map(v => (
            <VacationCard key={v.vacation_id} vacation={v} onDelete={handleDelete} />
          ))}
        </div>
      </div>
    </div>
  )
}
