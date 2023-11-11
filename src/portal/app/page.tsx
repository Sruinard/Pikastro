import Image from "next/image";

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <div className="z-10 max-w-5xl w-full items-center justify-between font-mono text-sm lg:flex">
        <div className="fixed bottom-0 left-0 flex h-48 w-full items-end justify-center bg-gradient-to-t from-white via-white dark:from-black dark:via-black lg:static lg:h-auto lg:w-auto lg:bg-none">
          <a
            className="pointer-events-none flex place-items-center gap-2 p-8 lg:pointer-events-auto lg:p-0"
            href="https://vercel.com?utm_source=create-next-app&utm_medium=appdir-template&utm_campaign=create-next-app"
            target="_blank"
            rel="noopener noreferrer"
          >
            By Pikastro - Renewable Energy Made Profitable
          </a>
        </div>
        <div className="flex flex-col items-center justify-center gap-8 lg:flex-row">
          <div className="flex flex-col items-center justify-center gap-4">
            {/* sign in/sign up */}
            <div className="flex items-center justify-center gap-4">
              <a
                href="/signin"
                className="px-6 py-2 text-sm font-medium text-center text-white transition-colors duration-200 transform bg-gradient-to-r from-blue-600 to-blue-900 rounded-md hover:from-blue-500 hover:to-blue-700 focus:ring focus:ring-blue-500 focus:ring-opacity-50"
              >
                Sign In
              </a>
              <a
                href="/signup"
                className="px-6 py-2 text-sm font-medium text-center text-white transition-colors duration-200 transform bg-gradient-to-r from-blue-600 to-blue-900 rounded-md hover:from-blue-500 hover:to-blue-700 focus:ring focus:ring-blue-500 focus:ring-opacity-50"
              >
                Sign Up
              </a>
            </div>
          </div>
        </div>
      </div>

      <div className="relative flex place-items-center before:absolute before:h-[300px] before:w-[480px] before:-translate-x-1/2 before:rounded-full before:bg-gradient-radial before:from-white before:to-transparent before:blur-2xl before:content-[''] after:absolute after:-z-20 after:h-[180px] after:w-[240px] after:translate-x-1/3 after:bg-gradient-conic after:from-sky-200 after:via-blue-200 after:blur-2xl after:content-[''] before:dark:bg-gradient-to-br before:dark:from-transparent before:dark:to-blue-700 before:dark:opacity-10 after:dark:from-sky-900 after:dark:via-[#0141ff] after:dark:opacity-40 before:lg:h-[360px] z-[-1]">
        <p className="text-center">
          <span className="text-6xl font-bold dark:text-white">Pikastro</span>
          <br />
          <span className="text-4xl font-bold dark:text-white">
            Solar Energy Made Profitable
          </span>
        </p>
      </div>

      <div className="mb-32 grid text-center lg:max-w-5xl lg:w-full lg:mb-0 lg:grid-cols-4 lg:text-left"></div>
    </main>
  );
}
