import React, { useState, useEffect } from 'react';

const ChartComponent = () => {
  const [content, setContent] = useState(<span className="loading loading-infinity loading-lg"></span>);

  useEffect(() => {
    fetch('http://178.128.227.84')
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json(); // or response.json() if the server responds with JSON
      })
      .then(data => {
        // Assuming the response data is the content you want to display
        setContent(<div>{data.message}</div>);
      })
      .catch(error => {
        // Handle the error case
        console.error('There was an error!', error);
      });
  }, []);

  return (
    <div id="chart" className="flex flex-wrap justify-center gap-8">
      {content}
    </div>
  );
};

export default ChartComponent;
