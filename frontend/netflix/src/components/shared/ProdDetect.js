export default function isProd() {
    return !process.env.REACT_APP_PROD || process.env.REACT_APP_PROD === 'true';
}