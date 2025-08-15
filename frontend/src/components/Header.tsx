export default function Header() {
    return (
        <>
            <div className="w-screen h-16 bg-darkSlate flex justify-between items-center fixed top-0 left-0 right-0 z-50 font-pressStart box-border px-4">
                <div className="flex justify-evenly items-center w-auto">
                    Logo Here
                    <h1 className="text-xl ml-2 text-offWhite">Big Bear's Cave</h1>
                </div>
                <div className="flex justify-evenly items-center gap-4">
                    <div className="text-offWhite hover:text-magicBlue cursor-pointer">
                        Início
                    </div>
                    <div className="text-offWhite hover:text-magicBlue cursor-pointer">
                        Sobre
                    </div>
                </div>
            </div>
        </>
    );
}