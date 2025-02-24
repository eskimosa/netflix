import React from "react";
import Main from "../components/Main";
import Row from "../components/Row";
import baseUrl from "../components/shared/baseUrl";
import requests from "../Requests";
import { useState, useEffect } from "react";
import axios from "axios";


const Home = () => {
  const [trending, setTrending] = useState([]);
  const [topRated, setTopRated] = useState([]);
  const [upcoming, setUpcoming] = useState([]);
  const [popular, setPopular] = useState([]);
  const [horror, setHorror] = useState([]);
  const [loading, setLoading] = useState(true);

  const key = "YOUR_API_KEY";

  useEffect(() => {
    const fetchMovieData = async () => {
      try {
        // Fetch trending movies
        const trendingResponse = await axios.get(
          `${baseUrl}/api/list_trending/`
        );
        setTrending(trendingResponse.data);

        // Fetch top-rated movies
        const topRatedResponse = await axios.get(
          `${baseUrl}/api/list_top_rated/`
        );
        setTopRated(topRatedResponse.data);

        // Fetch upcoming movies
        const upcomingResponse = await axios.get(
          `${baseUrl}/api/list_upcoming/`
        );
        setUpcoming(upcomingResponse.data);

        const popularResponse = await axios.get(`${baseUrl}/api/list_popular/`);
        setPopular(popularResponse.data);

        const horrorResponse = await axios.get(
          `https://api.themoviedb.org/3/discover/movie?api_key=${key}&with_genres=27&language=en-US&page=1&include_adult=false`
        );
        setHorror(horrorResponse.data.results);

        setLoading(false);
      } catch (error) {
        console.error("Error fetching movie data:", error);
        setLoading(false);
      }
    };

    fetchMovieData();
  }, []);

  if (loading) {
    return <div>Loading...</div>;
  }

  return (
    <>
      <Main />
      <Row rowID="1" title="Top Rated" movies={topRated} />
      <Row rowID="2" title="UpComing" movies={upcoming} />
      <Row rowID="3" title="Popular" movies={popular} />
      <Row rowID="4" title="Trending" movies={trending} />
      <Row rowID="5" title="Horror" movies={horror} />
    </>
  );
};

export default Home;
