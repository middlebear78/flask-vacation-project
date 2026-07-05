import { useEffect, useState } from 'react'

export default function BackToTop() {
  const [visible, setVisible] = useState(false)

  useEffect(() => {
    function onScroll() {
      setVisible(window.scrollY > 300)
    }
    window.addEventListener('scroll', onScroll)
    return () => window.removeEventListener('scroll', onScroll)
  }, [])

  function scrollToTop(e) {
    e.preventDefault()
    window.scrollTo({ top: 0, behavior: 'smooth' })
  }

  return (
    <a
      href="#"
      className="btn btn-lg btn-primary btn-lg-square back-to-top"
      onClick={scrollToTop}
      style={{ display: visible ? 'flex' : 'none' }}
    >
      <i className="bi bi-arrow-up"></i>
    </a>
  )
}
