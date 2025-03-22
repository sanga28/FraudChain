import Navbar from "../components/Navbar";

const Home = () => {
  return (
    <div>
      <Navbar />
      <div className="container">
        <h1>Welcome to FraudChain</h1>
        <p>Blockchain-powered fraud detection system.</p>
      </div>
    </div>
  );
};

export default Home;
