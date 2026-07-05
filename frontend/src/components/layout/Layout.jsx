import { Outlet } from 'react-router-dom'
import TopBar from './TopBar'
import Navbar from './Navbar'
import Footer from './Footer'
import BackToTop from './BackToTop'
import FlashMessage from '../common/FlashMessage'

export default function Layout() {
  return (
    <>
      <FlashMessage />
      <header>
        <TopBar />
      </header>
      <nav>
        <Navbar />
      </nav>
      <main>
        <Outlet />
      </main>
      <footer>
        <Footer />
      </footer>
      <BackToTop />
    </>
  )
}
