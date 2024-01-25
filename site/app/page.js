import Image from "next/image";

export default function Home() {
  return (
    <div>
      <header className="bg-gray-800 text-white">
        <div className="container mx-auto p-4 flex justify-between items-center">
          <h1 className="text-xl font-bold">Tech Job Insights</h1>
          <nav>
            <ul className="flex space-x-4">
              <li><a href="#home" className="hover:text-gray-300">Home</a></li>
              <li><a href="#about" className="hover:text-gray-300">About</a></li>
              <li><a href="#contact" className="hover:text-gray-300">Contact</a></li>
            </ul>
          </nav>
        </div>
      </header>

      <main className="container mx-auto p-4">
        <section id="home" className="text-center my-12">
          <h2 className="text-3xl font-bold mb-4">Welcome to Tech Job Insights</h2>
          <p className="text-xl">Discover the latest trends and insights in the technology job market.</p>
        </section>

        {/* Add more sections here as needed */}
      </main>

      <footer className="bg-gray-700 text-white text-center p-4">
        <p>&copy; {new Date().getFullYear()} Tech Job Insights. All rights reserved.</p>
      </footer>
    </div>
  );
}
