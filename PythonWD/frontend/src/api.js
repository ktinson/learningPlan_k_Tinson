let apiURL;

if (process.env.NODE_ENV === "development") {
  apiURL = process.env.REACT_APP_API_URL|| "http://localhost:8000" 
} else if(process.env.NODE_ENV === "production") {
  apiURL = "https://learningplan-k-tinson.onrender.com";
}else{
  console.log("erorororo ")
}
// || "https://learningplan-k-tinson.onrender.com";
export default apiURL;
