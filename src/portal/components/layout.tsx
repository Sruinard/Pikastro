import React from "react";
import Sidebar from "@/components/sidebar";

export default function Layout({ children }: { children: React.ReactNode }) {
  return (
    <div className="flex flex-row w-full h-screen">
      <Sidebar />
      <div className="flex flex-col flex-grow">{children}</div>
    </div>
  );
}
