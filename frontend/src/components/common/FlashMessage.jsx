import { useFlash } from '../../context/FlashContext'

export default function FlashMessage() {
  const { flash } = useFlash()

  if (!flash) return null

  const className = flash.category === 'error' || flash.category === 'danger'
    ? 'error'
    : flash.category === 'success'
      ? 'user-login'
      : 'messages'

  return (
    <div className={className}>
      {flash.message}
    </div>
  )
}
