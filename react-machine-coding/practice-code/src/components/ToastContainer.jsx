import React, { useState, useRef } from "react";
import "../App.css";

/**
 * Toast Container — complete logic in one read:
 *
 * Multiple toasts are stored in `toasts` state as an array of { id, message, type }.
 * Each toast auto-dismisses after 5 seconds. Timer IDs live in `timersRef` so we can
 * cancel them on manual close and avoid stale timeouts firing after unmount.
 *
 * Quick function review:
 *   handleAdd(message, type)
 *     → Creates a unique id (timestamp), appends a new toast to state,
 *       and starts a 5s setTimeout that calls handleClose(id).
 *
 *   handleClose(id)
 *     → Clears and deletes that toast's timer from timersRef,
 *       then removes the toast from state via filter (functional update).
 *
 *   Render
 *     → Maps `toasts` into styled toast divs (class = type: success/info/warning/error).
 *       "x" click calls handleClose(id). Buttons call handleAdd with preset message + type.
 */

function ToastContainer() {
  const [toasts, setToasts] = useState([]);
  const timersRef = useRef({});

  const handleClose = (id) => {
    clearTimeout(timersRef.current[id]);
    delete timersRef.current[id];

    setToasts((prevToasts) => {
      const filteredArr = prevToasts.filter((toast) => {
        return toast.id !== id;
      });
      return filteredArr;
    });
  };

  const handleAdd = (message, type) => {
    const id = new Date().getTime();
    const newToasts = [...toasts, { id, message, type }];
    setToasts(newToasts);
    timersRef.current[id] = setTimeout(() => handleClose(id), 5000);
  };

  return (
    <div className="container">
      <div className="toast-container">
        {toasts.map(({ id, message, type }) => {
          return (
            <div key={id} className={`toast ${type}`}>
              {message} <span onClick={() => handleClose(id)}>x</span>
            </div>
          );
        })}
      </div>
      <div className="btn-container">
        <button onClick={() => handleAdd("Success", "success")}>
          Success Toast
        </button>
        <button onClick={() => handleAdd("Info", "info")}>Info Toast</button>
        <button onClick={() => handleAdd("Warning", "warning")}>
          Warning Toast
        </button>
        <button onClick={() => handleAdd("Error", "error")}>Error Toast</button>
      </div>
    </div>
  );
}

export default ToastContainer;
