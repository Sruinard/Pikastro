export default function ChatWindow({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <div className="flex flex-col w-full h-screen overflow-auto">
      <div className="h-screen border-r flex flex-col items-center justify-center  border-gray-200 dark:border-gray-700">
        {children}
      </div>
    </div>
  );
}
