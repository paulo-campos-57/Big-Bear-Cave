import { useNavigate } from "react-router-dom";

export default function Header() {
    const navigate = useNavigate();

    return (
        <>
            <div className="w-screen h-16 bg-darkSlate flex justify-between items-center fixed top-0 left-0 right-0 z-50 font-pressStart box-border px-4">
                <div className="flex justify-evenly items-center w-auto">
                    <img src="/images/logoBear.png" className="w-20" />
                    <h1 className="text-xl ml-2 text-offWhite">Big Bear's Cave</h1>
                </div>
                <div className="flex justify-evenly items-center gap-4">
                    <div className="text-offWhite hover:text-magicBlue cursor-pointer"
                        onClick={() => navigate('/')}>
                        Início
                    </div>
                    <div className="text-offWhite hover:text-magicBlue cursor-pointer">
                        Sobre
                    </div>
                    <div className="text-offWhite hover:text-magicBlue cursor-pointer"
                        onClick={() => navigate('/cadastro')}>
                        Cadastro
                    </div>
                </div>
            </div>
        </>
    );
}