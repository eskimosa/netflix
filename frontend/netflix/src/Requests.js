import baseUrl from "./components/shared/baseUrl";

const requests = {
    requestPopular: `${baseUrl}/api/list_popular/`,
    requestTrending: `${baseUrl}/api/list_trending/`,
    requestUpcoming: `${baseUrl}/api/list_upcoming/`,
    requestTopRated: `${baseUrl}/api/list_top_rated/`,
};

export default requests;