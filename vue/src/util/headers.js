const getCookie = (name) => {
  if (typeof document === "undefined") {
    return null;
  }
  let cookieValue = null;
  if (document.cookie && document.cookie != "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = $.trim(cookies[i]);
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) == (name + "=")) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
};

const getCSRFToken = () => getCookie('csrftoken');

const csrf = {
  getCookie,
  getCSRFToken
};

export const safeHeaders = {
  Accept: "application/json"
};

export const unsafeHeaders = {
  "Accept": "application/json",
  "Content-Type": "application/json",
  "X-CSRFToken": csrf.getCSRFToken()
};

export const uploadHeaders = {
  "Accept": "application/json",
  "X-CSRFToken": csrf.getCSRFToken()
};

export default csrf;
