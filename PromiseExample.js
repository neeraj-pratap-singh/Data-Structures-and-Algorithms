function fetchData(url) {
    return new Promise((resolve, reject) => {
      setTimeout(() => {
      
       const data = { message: "Data fetched successfully from " + url };
        resolve(data);
        reject("error");
      }, 1000);
    });
  }
  
  // Promise chaining example
  // fetchData("first-url")
  //   .then((result1) => {
  //     console.log(result1.message);
  
  //     return fetchData("second-url");
  //   })
  //   .then((result2) => {
  //     console.log(result2.message);
  
  //     return fetchData("third-url");
  //   })
  //   .then((result3) => {
  //     console.log(result3.message);
  //   })
  //   .catch((error) => {
  //     console.error("Error:", error.message);
  //   });
  
  async function fetchDataAsync() {
    try {
      const result1 = await fetchData('first-url');
      console.log(result1.message);
  
      const result2 = await fetchData('second-url');
      console.log(result2.message);
  
      const result3 = await fetchData('third-url');
      console.log(result3.message);
    } catch (error) {
      console.error('Error:', error.message);
    }
}

fetchDataAsync()