import isProd from "./ProdDetect";

let baseUrl = '';
if (isProd()) {
    baseUrl = 'http://localhost:8000';
} else {
    baseUrl = 'http://localhost:8000';
}

console.log(`REACT_APP_PROD: ${process.env.REACT_APP_PROD}`);
console.log(`Base URL: ${baseUrl}`);
export default baseUrl;