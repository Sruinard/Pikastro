import React from "react";

interface NavLink {
  name: string;
  href: string;
}

export default function Sidebar() {
  const links: NavLink[] = [
    { name: "Home", href: "/" },
    { name: "Sign In", href: "/signin" },
    { name: "Sign Up", href: "/signup" },
  ];
  return (
    <div className="flex flex-col w-64 h-screen px-4 py-8 bg-white border-r dark:bg-gray-800 dark:border-gray-600">
      {links.map((link, k) => (
        <a
          key={k}
          href="#"
          className="flex items-center mt-4 py-2 px-6 bg-gray-200 bg-opacity-25 text-gray-700 dark:bg-gray-900 dark:bg-opacity-25 dark:text-gray-100"
        >
          <span className="mx-4 text-lg font-normal">{link.name}</span>
        </a>
      ))}

      <div className="flex items-center mt-auto">
        <button className="flex items-center justify-center w-full py-3 px-6 font-medium text-white bg-gray-700 rounded-md dark:bg-gray-800 dark:text-gray-200">
          Create account
        </button>
      </div>
    </div>
  );
}
