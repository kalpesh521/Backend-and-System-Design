import { useState } from 'react' 
import './App.css'
import Otp from './components/Otp'
import ToastContainer from './components/ToastContainer'
import Stepper from './components/Stepper'
function App() { 

  const steps = [
    {
      label: "Personal Info",
      content: <div>Personal Information Content</div>,
    },
    {
      label: "Account Info",
      content: <div>Account Info Content</div>,
    },
    {
      label: "Payment",
      content: <div>Payment Content</div>,
    },
    {
      label: "Confirmation",
      content: <div>Confirmation Content</div>,
    },
    {
      label: "Review",
      content: <div>Review Content</div>,
    },
  ];

  return (
    <>
      {/* <Otp /> */}
      {/* <ToastContainer />   */}
      <Stepper steps={steps} />
    </>
  )
}

export default App
