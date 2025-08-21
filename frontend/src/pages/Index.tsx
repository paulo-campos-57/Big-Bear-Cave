import { useNavigate } from "react-router-dom";
import Footer from "../components/Footer";
import Header from "../components/Header";

export default function Index() {
    const navigate = useNavigate();
    
    return (
        <>
            <div className="font-pressStart w-screen h-screen bg-charcoal flex flex-col">
                <Header />

                <div className="flex flex-1">
                    <div className="bg-darkSlate w-1/2 flex flex-col justify-center items-center gap-7">
                        <h1 className="text-2xl text-offWhite">Bem vindo à Caverna!</h1>
                        <img src="/images/logoBear.png" className="w-80" />
                        <p className="text-offWhite">O hub dos jogadores!</p>
                    </div>

                    <div className="bg-charcoal w-1/2 flex flex-col justify-center items-center gap-5">
                        <h2 className="text-xl text-offWhite">Login</h2>
                        <form className="h-1/2 bg-darkSlate flex flex-col justify-center items-center rounded gap-4 w-2/3">
                            <input
                                type="email"
                                placeholder="Email"
                                className="p-3 rounded bg-charcoal text-offWhite focus:outline-none"
                            />
                            <input
                                type="password"
                                placeholder="Senha"
                                className="p-3 rounded bg-charcoal text-offWhite focus:outline-none"
                            />
                            <button
                                type="submit"
                                className="bg-deepRed text-offWhite p-3 rounded hover:bg-forestGreen transition"
                            >
                                Entrar
                            </button>
                        </form>
                        <p className="text-offWhite text-sm">
                            Ainda não tem conta? <span className="text-golden hover:text-forestGreen cursor-pointer"
                                onClick={() => navigate("/cadastro")}>Cadastre-se</span>
                        </p>
                    </div>
                </div>

                <Footer />
            </div>
        </>
    );
}
