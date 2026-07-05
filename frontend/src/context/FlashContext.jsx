import { createContext, useContext, useState, useCallback } from 'react'

const FlashContext = createContext(null)

export function FlashProvider({ children }) {
  const [flash, setFlash] = useState(null)

  const showFlash = useCallback((message, category = 'info') => {
    setFlash({ message, category })
    setTimeout(() => setFlash(null), 3000)
  }, [])

  return (
    <FlashContext.Provider value={{ flash, showFlash }}>
      {children}
    </FlashContext.Provider>
  )
}

export function useFlash() {
  return useContext(FlashContext)
}
