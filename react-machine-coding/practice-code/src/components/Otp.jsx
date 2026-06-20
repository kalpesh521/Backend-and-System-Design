import React, { useState, useRef, useEffect } from "react";

/**
 * OTP Input — complete logic in one read:
 *
 * We render `otplength` separate input boxes, each holding one digit in `otpfield` state.
 * A `ref` array stores every input's DOM node so we can programmatically move focus between boxes.
 * On mount, the first input is auto-focused. On each key press, `handleKeyDown` runs:
 *   - Arrow Left/Right → jump focus to the previous/next box (within bounds).
 *   - Backspace → clear the current box and move focus to the previous one.
 *   - Any non-numeric key → ignored.
 *   - A valid digit → saved in the current box, then focus auto-moves to the next box.
 * State is always updated via a copied array (never mutated directly), and each input's
 * ref callback registers itself into `ref.current[index]` for focus control.
 */

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
