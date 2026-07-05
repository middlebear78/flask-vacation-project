const BASE = ''

async function request(url, options = {}) {
  const res = await fetch(BASE + url, {
    credentials: 'include',
    ...options,
  })
  const data = await res.json()
  if (!res.ok) {
    throw new Error(data.error || 'Request failed')
  }
  return data
}

function jsonRequest(url, method, body) {
  return request(url, {
    method,
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body),
  })
}

// Auth
export function login(email, password) {
  return jsonRequest('/api/auth/login', 'POST', { email, password })
}

export function register(first_name, last_name, email, password) {
  return jsonRequest('/api/auth/register', 'POST', { first_name, last_name, email, password })
}

export function logout() {
  return jsonRequest('/api/auth/logout', 'POST', {})
}

export function getMe() {
  return request('/api/auth/me')
}

// Vacations
export function getVacations() {
  return request('/api/vacations/')
}

export function getVacation(id) {
  return request('/api/vacations/' + id)
}

export function createVacation(formData) {
  return request('/api/vacations/', {
    method: 'POST',
    body: formData,
  })
}

export function updateVacation(id, formData) {
  return request('/api/vacations/' + id, {
    method: 'PUT',
    body: formData,
  })
}

export function deleteVacation(id) {
  return request('/api/vacations/' + id, { method: 'DELETE' })
}

export function likeVacation(id) {
  return request('/api/vacations/' + id + '/like', { method: 'POST' })
}

export function unlikeVacation(id) {
  return request('/api/vacations/' + id + '/like', { method: 'DELETE' })
}

export function vacationImageUrl(imageName) {
  if (!imageName) return '/images/no-image.png'
  return '/api/vacations/images/' + imageName
}

// Countries
export function getCountries() {
  return request('/api/countries/')
}
