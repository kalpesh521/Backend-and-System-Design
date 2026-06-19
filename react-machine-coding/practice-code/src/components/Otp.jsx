import React, { useState, useRef, useEffect } from "react";

function Otp({ otplength = 6 }) {
  const [otpfield, setOtpField] = useState(new Array(otplength).fill(""));
  const ref = useRef([]);

  const handleKeyDown = (e, index) => {
    const copyOtpField = [...otpfield];
    const key = e.key;

    if (key === "ArrowLeft") {
      if (index > 0) ref.current[index - 1].focus();
      return;
    }
    if (key === "ArrowRight") {
      if (index + 1 < otpfield.length) ref.current[index + 1].focus();
      return;
    }

    if (key === "Backspace") {
      copyOtpField[index] = "";
      setOtpField(copyOtpField);

      if (index > 0) {
        ref.current[index - 1].focus();
      }
      return;
    }
    if (isNaN(key)) {
      return;
    }

    copyOtpField[index] = key;

    if (index + 1 < otpfield.length) {
      ref.current[index + 1].focus();
    }

    setOtpField(copyOtpField);
  };

  useEffect(() => {
    ref.current[0].focus();
  }, []);
  return (
    <>
      {otpfield.map((value, index) => {
        return (
          <input
            type="text"
            value={value}
            ref={(currentInput) => (ref.current[index] = currentInput)}
            key={index}
            onKeyDown={(e) => handleKeyDown(e, index)}
          />
        );
      })}
    </>
  );
}

export default Otp;
