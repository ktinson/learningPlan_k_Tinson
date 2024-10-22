let apiURL;

if (process.env.NODE_ENV === "development") {
  apiURL = process.env.REACT_APP_API_URL || "http://localhost:8000";
} else {
  apiURL = "https://learningplan-k-tinson.onrender.com";
}
// || "https://learningplan-k-tinson.onrender.com";
export default apiURL;
