import React from "react";
import Main from "../components/Main";
import Row from "../components/Row";
import baseUrl from "../components/shared/baseUrl";
import requests from "../Requests";
import { useState, useEffect } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../components/AuthProvider";
import api from "../components/axiosConfig";

const HomeAuth = () => {
  const { user } = useAuth();
  const [trending, setTrending] = useState([]);
  const [topRated, setTopRated] = useState([]);
  const [upcoming, setUpcoming] = useState([]);
  const [popular, setPopular] = useState([]);
  const [horror, setHorror] = useState([]);
  const [favorites, setFavorites] = useState([]);
  const [loading, setLoading] = useState(true);

  const navigate = useNavigate();


  useEffect(() => {
    const fetchMovieData = async () => {
      try {
        const trendingResponse = await axios.get(requests.requestTrending);
        setTrending(trendingResponse.data);

        const topRatedResponse = await axios.get(requests.requestTopRated);
        setTopRated(topRatedResponse.data);

        const upcomingResponse = await axios.get(requests.requestUpcoming);
        setUpcoming(upcomingResponse.data);

        const popularResponse = await axios.get(requests.requestPopular);
        setPopular(popularResponse.data);

        const horrorResponse = await axios.get(requests.requestHorror);
        setHorror(horrorResponse.data.results);

        if (user) {
          const favoritesResponse = await api.get("/api/list_popular/");
          setFavorites(favoritesResponse.data);
        }

        setLoading(false);
      } catch (error) {
        console.error("Error fetching movie data:", error);
        setLoading(false);
      }
    };

    fetchMovieData();
  }, [user]);

  if (loading) {
    return <div>Loading...</div>;
  }

  return (
    <>
      <Main />
      {user && <Row rowID="1" title="Favorites" movies={favorites} />}
      <Row rowID="2" title="Top Rated" movies={topRated} />
      <Row rowID="3" title="UpComing" movies={upcoming} />
      <Row rowID="4" title="Popular" movies={popular} />
      <Row rowID="5" title="Trending" movies={trending} />
      <Row rowID="6" title="Horror" movies={horror} />
    </>
  );
};

export default HomeAuth;
