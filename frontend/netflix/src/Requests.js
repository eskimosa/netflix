import baseUrl from "./components/shared/baseUrl";

const key = 'YOUR_API_KEY';

const requests = {
    requestPopular: `${baseUrl}/api/list_popular/`,
    requestTrending: `${baseUrl}/api/list_trending/`,
    requestHorror: `https://api.themoviedb.org/3/discover/movie?api_key=${key}&with_genres=27&language=en-US&page=1&include_adult=false`,
    requestUpcoming: `${baseUrl}/api/list_upcoming/`,
    requestTopRated: `${baseUrl}/api/list_top_rated/`,
};

export default requests;