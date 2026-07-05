import { BrowserRouter, Routes, Route } from 'react-router-dom'
import { AuthProvider } from './context/AuthContext'
import { FlashProvider } from './context/FlashContext'
import Layout from './components/layout/Layout'
import ProtectedRoute from './components/ProtectedRoute'
import AdminRoute from './components/AdminRoute'

import HomePage from './pages/HomePage'
import AboutPage from './pages/AboutPage'
import LoginPage from './pages/LoginPage'
import RegisterPage from './pages/RegisterPage'
import VacationsPage from './pages/VacationsPage'
import AddVacationPage from './pages/AddVacationPage'
import EditVacationPage from './pages/EditVacationPage'
import NotFoundPage from './pages/NotFoundPage'

export default function App() {
  return (
    <BrowserRouter>
      <FlashProvider>
        <AuthProvider>
          <Routes>
            <Route element={<Layout />}>
              <Route path="/" element={<HomePage />} />
              <Route path="/about" element={<AboutPage />} />
              <Route path="/login" element={<LoginPage />} />
              <Route path="/register" element={<RegisterPage />} />
              <Route path="/vacations" element={
                <ProtectedRoute><VacationsPage /></ProtectedRoute>
              } />
              <Route path="/vacations/new" element={
                <AdminRoute><AddVacationPage /></AdminRoute>
              } />
              <Route path="/vacations/edit/:id" element={
                <AdminRoute><EditVacationPage /></AdminRoute>
              } />
              <Route path="*" element={<NotFoundPage />} />
            </Route>
          </Routes>
        </AuthProvider>
      </FlashProvider>
    </BrowserRouter>
  )
}
