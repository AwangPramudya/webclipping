import "./globals.css";

export const metadata = {
  title: "Web Clipping",
  description: "Simple web clipping tool",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
