import Header from "../components/Header";

export default function Index() {
    return(
        <>
            <div className="w-screen h-screen bg-charcoal flex flex-col items-center justify-center">
                <Header />
                <h1 className="font-pressStart text-2xl text-offWhite">Lorem Ipsum</h1>
            </div>
        </>
    );
}