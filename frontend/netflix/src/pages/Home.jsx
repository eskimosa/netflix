import React from 'react'
import Main from '../components/Main'
import Row from '../components/Row'
import baseUrl from '../components/shared/baseUrl'
import requests from '../Requests'

const Home = () => {
  return (
    <>
        <Main />
        {/* <Row title='Top Rated' fetchURL={`${baseUrl}/api/movies/`} /> */}
        <Row rowID='1' title='Top Rated' fetchURL={requests.requestTopRated} />
        <Row rowID='2' title='UpComing' fetchURL={requests.requestUpcoming} />
        <Row rowID='3' title='Popular' fetchURL={requests.requestPopular} />
        <Row rowID='4' title='Trending' fetchURL={requests.requestTrending} />
        <Row rowID='5' title='Horror' fetchURL={requests.requestHorror} />
    </>
  )
}

export default Home