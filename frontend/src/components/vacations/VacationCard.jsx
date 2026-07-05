import { useState } from 'react'
import { Link } from 'react-router-dom'
import { useAuth } from '../../context/AuthContext'
import { useFlash } from '../../context/FlashContext'
import * as api from '../../api/client'

export default function VacationCard({ vacation, onDelete }) {
  const { user } = useAuth()
  const { showFlash } = useFlash()
  const [liked, setLiked] = useState(vacation.is_liked)
  const [likes, setLikes] = useState(vacation.likes)

  async function toggleLike() {
    const prevLiked = liked
    const prevLikes = likes

    // Optimistic update
    setLiked(!liked)
    setLikes(liked ? likes - 1 : likes + 1)

    try {
      const result = liked
        ? await api.unlikeVacation(vacation.vacation_id)
        : await api.likeVacation(vacation.vacation_id)
      setLikes(result.likes)
    } catch (err) {
      // Revert on error
      setLiked(prevLiked)
      setLikes(prevLikes)
      showFlash(err.message, 'error')
    }
  }

  async function handleDelete() {
    if (!window.confirm('Are you sure?')) return
    try {
      await api.deleteVacation(vacation.vacation_id)
      onDelete(vacation.vacation_id)
    } catch (err) {
      showFlash(err.message, 'error')
    }
  }

  return (
    <div className="col-lg-4 col-md-6" data-aos="fade-up">
      <div className="package-item">
        <button
          onClick={!user.is_admin ? toggleLike : undefined}
          className={`btn btn-like-custom ${user.is_admin ? 'disabled-btn' : ''}`}
          disabled={user.is_admin}
        >
          <i className={`${liked ? 'fas liked' : 'far'} fa-heart icon-heart-custom`}></i>
        </button>

        <small className="text-primary me-2 count-likes-custom">
          Likes&nbsp;<span className="count-likes-value">{likes}</span>
        </small>

        <div className="text-center p-4">
          <h2 className="mb-0">{vacation.vacation_name}</h2>
        </div>

        <div className="overflow-hidden">
          <img className="img-fluid" src={api.vacationImageUrl(vacation.vacation_img)} alt="vacation image" />
        </div>

        <div className="d-flex border-bottom">
          <small className="flex-fill text-center border-end py-2">
            <i className="fa fa-map-marker-alt text-primary me-2"></i>{vacation.country_name}
          </small>
          <small className="flex-fill text-center border-end py-2">
            <i className="fa fa-calendar-alt text-primary me-2"></i>{vacation.vacation_days} days
          </small>
          <small className="flex-fill text-center py-2">
            <i className="fa fa-user text-primary me-2"></i>2 Person
          </small>
        </div>

        <div className="d-flex border-bottom">
          <small className="flex-fill text-center border-end py-2">
            <i className="fa fa-calendar-alt text-primary me-2"></i>Start: {vacation.start_date}
          </small>
          <small className="flex-fill text-center border-end py-2">
            <i className="fa fa-calendar-alt text-primary me-2"></i>Ends: {vacation.end_date}
          </small>
        </div>

        <div className="text-center p-4">
          <h3 className="mb-0">${vacation.price}</h3>
          <div className="mb-3">
            {[...Array(5)].map((_, i) => (
              <small key={i} className="fa fa-star text-primary"></small>
            ))}
          </div>
          <div className="vacation-description-scroll">
            <p>{vacation.vacation_description}</p>
          </div>
          {user.is_admin && (
            <div className="d-flex justify-content-center mb-2">
              <Link
                to={`/vacations/edit/${vacation.vacation_id}`}
                className="btn btn-sm btn-primary px-3 border-end"
                style={{ borderRadius: '30px 0 0 30px' }}
              >
                &nbsp;&nbsp;&nbsp;Edit&nbsp;
              </Link>
              <button
                onClick={handleDelete}
                className="btn btn-sm btn-primary px-3"
                style={{ borderRadius: '0 30px 30px 0' }}
              >
                Delete
              </button>
            </div>
          )}
        </div>
      </div>
    </div>
  )
}
